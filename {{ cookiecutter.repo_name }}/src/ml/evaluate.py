def evaluate_model(est, x_tr, y_tr, x_ho, y_ho, **kwargs):
    pred_tr = est.predict(x_tr)
    score_tr = balanced_accuracy_score(y_tr, pred_tr)
    pred_ho = est.predict(x_ho)
    score_ho = balanced_accuracy_score(y_ho, pred_ho)
    return {'score-tr': score_tr, 'score-ho': score_ho}


def evaluate_model(mdl, data, metric):
    mdl.verbose = 0
    tr_pred = mdl.predict(data['x_tr'])
    te_pred = mdl.predict(data['x_te'])
    tr_score = metric(tr_pred, data['y_tr'].values)
    te_score = metric(te_pred, data['y_te'].values)
    print(f'train score {tr_score:3.2f}, test score {te_score:3.2f}')
