# Performing CV with xgboost]

* [Question posed and answered on DataScience.StackExchange](http://datascience.stackexchange.com/questions/6842/is-there-a-way-of-performing-stratified-cross-validation-using-xgboost-module-in?newsletter=1&nlcode=388111%7ca38a)
    * Relevant Excerpt:
            
        ```
        
        What you are doing is a typical example of k-fold cross validation.
        
        XGBoost is just used for boosting the performance and signifies "distributed gradient boosting".
        
        First, run the cross-validation step:
        
        kfld = sklearn.cross_validation.KFold(labels.size, n_folds=10)
        Then, use the train and test indices in kfld for constructing the XGBoost matrix and re-scaling weights by looping over them(the indices).
        
        A very neat implementation has been given as a Kaggle example [here](https://kaggle2.blob.core.windows.net/forum-message-attachments/44825/1290/test_xgboost.py?sv=2012-02-12&se=2015-12-14T21%3A28%3A18Z&sr=b&sp=r&sig=yQJmvA%2FpUqve9EDdkF1bWAaYjEtNFmcUfjQUHaTTD7U%3D).
        
        So, cross validation is not done with the xgboost package, it is done with the cross_validation module of sklearn, and then the gradient boosting is done on the indices of the k-fold validation variable results.
        
        ```
* Example code from Kaggle competition added [in this project](cv_xgboost/cv_xgboost.py)
