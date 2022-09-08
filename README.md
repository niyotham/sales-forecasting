# sales-forecasting
## Pharmaceutical sales prediction for multiple-stores



The finance team at Rossman wants to forecast sales in all thier stores across several cities six weeks 
ahead of time. This project is all about building and serving an end-to-end product that delivers this prediction to analysts in the finance team.

## Goal
 Build and serve an end-to-end product that delivers this prediction to analysts in the finance team.
 
 ## Store data exploration
Data exploratory analysis is done after combining the two datasets train and test and is found in eda file [notebooks/notebooks/eda_store.ipynb] (https://github.com/niyotham/sales-forecasting/blob/main/notebooks/eda_store.ipynb)

### Logging
[Logging](https://docs.python.org/3/howto/logging.html) is a way of tracking events that happen when you runa  software.
```
import logging
logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')
```
## Prediction of store sales
- Preprocessing
- Building models with sklearn pipelines
- Choose a loss function
- Post Prediction analysis
- Serialize models
- Building model with deep learning
- Using MLFlow to serve the prediction
## Serving predictions on a web interface
