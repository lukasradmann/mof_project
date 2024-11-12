import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.model_selection import train_test_split


'''
Trains the model on the 'train_data' and predicts the target variable on the 'test_data'.
'metric' is the evaluation metric used to train the model.
'sample' is a boolean variable that decides whether to sample the data or not.
'sample_size' is the size of the train_data, only used when 'sample' is True.
'time_limit' is the time limit for training the model.
'''
def train_test(df, metric, sample_size, time_limit):
    label = 'CO2_uptake_P0.15bar_T298K [mmol/g]'
    X_train, X_test = train_test_split(df, test_size=0.2, random_state=42)
    train_data = TabularDataset(X_train)
    test_data = TabularDataset(X_test)

    if sample_size:
        train_data = train_data.sample(n=sample_size, random_state=42)
        test_data = test_data.sample(n=sample_size, random_state=42)

    #train data
    predictor = TabularPredictor(label=label, eval_metric=metric).fit(train_data, time_limit=time_limit)
    #test data
    y_test = test_data[label]
    test_data_no_label = test_data.drop(columns=[label], axis=1)
    y_pred = predictor.predict(test_data_no_label)
    return [predictor, y_pred, y_test, test_data]

def evaluations(predictor, y_pred, y_test, test_data):
    scores = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)
    leaderboard = predictor.leaderboard(test_data)
    feature_importance = predictor.feature_importance(test_data)
    summary = predictor.fit_summary(verbosity=2)
    return scores, leaderboard, feature_importance, summary

def generate_report(train_test_outputs, sample_size, time_limit, report_path):
    scores, leaderboard, feature_importance, summary = evaluations(*train_test_outputs)

    with open(report_path, 'w') as f:
        if sample_size:
            f.write(f"Sample size, if any: {sample_size} \n")
        
        f.write(f"Time limit: {time_limit}\n")
        f.write("Evaluation Scores:\n")
        for metric, value in scores.items():
            f.write(f"{metric}: {value}\n")
        f.write("\nLeaderboard:\n")
        f.write(leaderboard.to_string(index=False))
        f.write("\n\nFeature Importance:\n")
        f.write(feature_importance.to_string(index=True))
        f.write("\n\nSummary:\n")
        for key, value in summary.items():
            f.write(f"{key}: {value}\n")


def main():
    df = pd.read_csv('../data/processed_MOFs.csv') 
    sample_size = 30000
    time_limit = 600 
    metric = 'mean_absolute_error'
    train_test_outputs = train_test(df, metric, sample_size, time_limit)

    #define report path and generate report
    report_path = train_test_outputs[0].path.split('AutogluonModels/')[-1]
    report_path = f'../reports/{report_path}.txt'
    generate_report(train_test_outputs, sample_size, time_limit, report_path)

if __name__ == "__main__":
    main()

