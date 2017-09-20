from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.structure import RecurrentNetwork
import pandas as pd
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader



def importaRedeTeste():
        net = NetworkReader.readFrom('rede-feedfoward.xml')
        print('pesos rede', net.params)
        dataset = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/intel_normalizado.txt')
        dataset_treino = SupervisedDataSet(8, 1)
        for i in range(dataset.__len__() - 1):
            dataset_treino.addSample(
                [dataset.iloc[i]['Open'], dataset.iloc[i]['High'], dataset.iloc[i]['Low'],
                 dataset.iloc[i]['Close'], dataset.iloc[i]['Volume'], dataset.iloc[i]['movel_26'],
                 dataset.iloc[i]['movel_10'], dataset.iloc[i]['MACD']], dataset.iloc[i + 1]['Open'])

        trainer = BackpropTrainer(net, dataset_treino, verbose=True, learningrate=0.01, momentum=0.99)
        for epoch in range(0, 10000):  # treina por 1000 iterações para ajuste de pesos
            resultTrainer = trainer.train()

        print(resultTrainer)
        test_data3 = SupervisedDataSet(8, 1)
        test_data3.addSample([37.87, 38.0, 37.52, 37.8, 32357313, 36.7930769231, 36.971, 0.17792307689999376],[37.82])  # saida 1 //erro //correct é a sequencia colocada e out e a saída da rede

        resultado1 = trainer.testOnData(test_data3, verbose=True)

def normalizaDataSet(nome_empresa):
    # Normalize time series data
    # load the dataset and print the first 5 rows
    series = pd.read_csv('~/Documentos/TCC/dist-tcc/Implementacao/dados_calculados/intel_normalizado.txt')
    print (series['Open-normalizado'].iloc[1])
    print (series.iloc[2]['Open'])
    net = NetworkReader.readFrom('rede-feedfoward.xml')
    print('pesos rede', net.params)
    dataset_treino = SupervisedDataSet(8, 1)
    for i in range(series.__len__() - 1):
        dataset_treino.addSample(
            [series.iloc[i]['Open-normalizado'], series.iloc[i]['High-normalizado'], series.iloc[i]['Low-normalizado'],
             series.iloc[i]['Close-normalizado'], series.iloc[i]['Volume-normalizado'], series.iloc[i]['movel_26-normalizado'],
             series.iloc[i]['movel_10-normalizado'], series.iloc[i]['MACD-normalizado']], series.iloc[i+1]['Open-normalizado'])

    trainer = BackpropTrainer(net, dataset_treino, verbose=True, learningrate=0.01, momentum=0.99)
    for epoch in range(0, 3000):  # treina por 1000 iterações para ajuste de pesos
        resultTrainer = trainer.train()

    NetworkWriter.writeToFile(net, 'rede2.xml')

    valor_abertura2 = (net.activate([37.87, 38.0, 37.52, 37.8, 32357313, 36.7930769231, 36.971,0.17792307689999376]))  # penultima - 1 #37.82 resultado #[ 0.90872757]
    print("valor abertura", valor_abertura2)
    resultadorede2 = valor_abertura2[0] * max(series['Open']) + (1 - valor_abertura2[0]) * min(series['Open'])
    print("resultado", resultadorede2)

    valor_abertura2 = (net.activate([37.82,37.92,37.42,37.56,34144843,36.8411538462,37.032,0.19084615379999548]))  # penultima - 1 #37.82 resultado #[ 0.90872757]
    print("valor abertura", valor_abertura2)
    resultadorede2 = valor_abertura2[0] * max(series['Open']) + (1 - valor_abertura2[0]) * min(series['Open'])
    print("resultado", resultadorede2)

    valor_abertura2 = (net.activate([38.0,38.45,37.81,37.98,44368566,36.8830769231,37.159,0.27592307689999984]))  # penultima - 1 #37.82 resultado #[ 0.90872757]
    print("valor abertura", valor_abertura2)
    resultadorede2 = valor_abertura2[0] * max(series['Open']) + (1 - valor_abertura2[0]) * min(series['Open'])
    print("resultado", resultadorede2)


if __name__ == '__main__':
    normalizaDataSet('intel')
