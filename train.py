from spin.utils import TrainOptions
from spin.train import Trainer

if __name__ == '__main__':
    options = TrainOptions().parse_args()
    trainer = Trainer(options)
    trainer.train()
