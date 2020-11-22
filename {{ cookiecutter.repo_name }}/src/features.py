


class TargetEncoding(BaseEstimator, TransformerMixin):
    def __init__(self, target='claps', group='site_id'):
        self.target = target
        self.group = group

    def fit(self, x, y=None):
        grps = x.groupby(self.group).mean().loc[:, self.target].to_frame()
        self.grps = grps.to_dict()[self.target]

        grps = x.groupby(self.group).count().loc[:, self.target].to_frame()
        self.freq_grps = grps.to_dict()[self.target]
        return self

    def transform(self, x):
        t = x.loc[:, self.group].replace(self.grps).to_frame()
        f = x.loc[:, self.group].replace(self.freq_grps).to_frame()
        return pd.concat([t, f], axis=1)

    def get_feature_names(self):
        return ['target-mean', 'target-freq']
