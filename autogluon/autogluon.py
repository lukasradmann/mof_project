import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor
from sklearn.model_selection import train_test_split


'''
This function trains a model on the provided 'train_data' and predicts the target variable on the 'test_data'.
'metric' specifies the evaluation metric used to train the model.
'sample_size' determines the number of samples to use from 'train_data' and 'test_data'.
'time_limit' is the maximum time allowed for model training.
'''
def train_test(train_data,test_data, metric, sample_size, time_limit):
    label = 'CO2_uptake_P0.15bar_T298K [mmol/g]'

    if sample_size:
        train_data = train_data.sample(n=sample_size, random_state=42)
        test_data = test_data.sample(n=sample_size, random_state=42)

    predictor = TabularPredictor(label=label, eval_metric=metric).fit(train_data, time_limit=time_limit)
    y_test = test_data[label]
    test_data_no_label = test_data.drop(columns=[label], axis=1)
    y_pred = predictor.predict(test_data_no_label)
    return [predictor, y_pred, y_test, test_data]

'''
different evaluations on the models performance
Running this function will generate a bokeh plot of different models and their performance.
'''
def evaluations(predictor, y_pred, y_test, test_data):
    scores = predictor.evaluate_predictions(y_true=y_test, y_pred=y_pred, auxiliary_metrics=True)
    leaderboard = predictor.leaderboard(test_data)
    feature_importance = predictor.feature_importance(test_data)
    summary = predictor.fit_summary(verbosity=2)
    return scores, leaderboard, feature_importance, summary

'''
generates a report based on the funciton 'evaluations'
report path is in 'reports' folder
'''  
def generate_report(train_test_outputs, sample_size, time_limit, report_path):
    scores, leaderboard, feature_importance, summary = evaluations(*train_test_outputs)

    with open(report_path, 'w') as f:
        if sample_size:
            f.write(f"Sample size, if any: {sample_size} \n")
        
        f.write(f"Time limit: {time_limit}\n")
        f.write("Evaluation Scores\n")
        for metric, value in scores.items():
            f.write(f"{metric}: {value}\n")
        f.write("\nLeaderboard:\n")
        f.write(leaderboard.to_string(index=False))
        f.write("\n\nFeature Importance:\n")
        f.write(feature_importance.to_string(index=True))
        f.write("\n\nSummary:\n")
        for key, value in summary.items():
            f.write(f"{key}: {value}\n")

# sample size, time limit and metric can be changed
def main():
    train_data = pd.read_csv('../data/train_MOFs.csv') 
    test_data = pd.read_csv('../data/test_MOFs.csv') 
    sample_size = False
    time_limit = 600 
    metric = 'mean_absolute_error'
    train_test_outputs = train_test(train_data,test_data, metric, sample_size, time_limit)

    #define report path and generate report
    report_path = train_test_outputs[0].path.split('AutogluonModels/')[-1]
    report_path = f'../reports/{report_path}.txt'
    generate_report(train_test_outputs, sample_size, time_limit, report_path)

if __name__ == "__main__":
    main()

