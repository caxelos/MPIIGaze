import torch
import numpy as np

# def load_checkpoint(filepath):
#     checkpoint = torch.load(filepath)
#     model = checkpoint['model']
#     model.load_state_dict(checkpoint['state_dict'])
#     for parameter in model.parameters():
#         parameter.requires_grad = False

#     model.eval()
#     return model

#model = load_checkpoint('results/resnet_preact/00/model_state.pth')
import importlib
module = importlib.import_module('models.zhang')#model_state_zhang.pth')#'models.resnet_preact')#models.{}'.format(args.arch))
model = module.Model()

checkpoint = torch.load('model_state_zhang.pth',map_location='cpu')
model.load_state_dict(checkpoint['state_dict'])
#model.load_state_dict('model_state_zhang.pth')#model.load_state_dict(torch.load('model_state.pt'))
model.eval()
img = torch.rand(1,1,60,36)
pose = torch.rand(1,2)
traced_script_module = torch.jit.trace(model, (img,pose))#gia multiple input:https://towardsdatascience.com/model-summary-in-pytorch-b5a1e4b64d25
traced_script_module.save('model.pt')



# #model = torch.load('results/resnet_preact/00/model_state.pth')
# model = TheModelClass(*args, **kwargs)
# model.load_state_dict(torch.load('model_state.pt'))
# model.eval()



#print(model): kati san to summary


#import torch
#from torchsummary import summary 
#summary(model,input_size=[(1,60,36),(1,2)])
