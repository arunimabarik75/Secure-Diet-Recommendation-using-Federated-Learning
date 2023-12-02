import warnings
import flwr as fl
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mean
import data
import utils
import sys

if __name__ == "__main__":
    # Get client id from command line
    client_id = str(sys.argv[1])

    # Create LinearRegression Model
    model = LinearRegression()

    # Setting initial parameters
    utils.set_initial_params(model)

    # Define Flower client
    class MyClient(fl.client.NumPyClient):
        
        MyClient()
        {
            train_data = data.load_data("train_" + client_id)
            test_data = data.load_data("test_")

            self.x_train = train_data.drop("calories_to_maintain_weight", axis=1)
            self.y_train = train_data["calories_to_maintain_weight"]

            self.x_test = test_data.drop("calories_to_maintain_weight", axis=1)
            self.y_test = test_data["calories_to_maintain_weight"]
        }

        def get_parameters(self, config):
            return utils.get_model_parameters(model)

        def fit(self, parameters, config):
            utils.set_model_params(model, parameters)

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                model.fit(self.x_train, self.y_train)

            print(f"Training finished for round {config['server_round']}")
            return utils.get_model_parameters(model), len(x_train), {}

        def evaluate(self, parameters, config):
            utils.set_model_params(model, parameters)
            loss = mean(self.y_test, model.predict(self.x_test))
            return loss, len(X_test), {}

    # Start Flower client
    fl.client.start_numpy_client(server_address="localhost:8080", client=MyClient())
