from __future__ import print_function

class CNNModel(object):
    def __init__(self, data_streamer, model):
        self.ds = data_streamer
        self.mean_train = self.ds.load_mean_train()
        self.model = model

    @staticmethod
    def preprocess(input_array, mean_train):
        input_array = input_array.astype('float32')
        input_array -= mean_train
        input_array /= 255.
        return input_array

    def predict_test(self, input_test_slices_arr):
        print("Preprocessing data.")
        test_slices_arr = self.preprocess(input_test_slices_arr, self.mean_train)
        print("Predicting the labelmap.")
        test_slices_prediction = self.model.predict(test_slices_arr, verbose=1)
        return test_slices_prediction
 
    def train(self, input_train_slices, input_train_segmentations, **kw_args):
        print("Preprocessing data.")
        train_slices_arr = self.preprocess(input_train_slices, self.mean_val, self.max_val)
        print("Training on the labelmap.")
        return self.model.fit(train_slices_arr, input_train_segmentations, verbose=1, shuffle = True, **kw_args)

