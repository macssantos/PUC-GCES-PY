import os
from parser.YAML_parser import YAMLParser
from parser.feature_engineering_parser import FeatureEngineeringParser
from parser.model_parser import ModelParser

def test_get_config():
    # Crie um arquivo YAML de exemplo em 'src/yamls' para testar a função
    yaml_content = """
    feature_engineering:
      - feature1
      - feature2
    model:
      algorithm: RandomForest
      parameters:
        n_estimators: 100
    """
    with open('src/yamls/test_config.yaml', 'w') as yaml_file:
        yaml_file.write(yaml_content)

    # Chame a função get_config e verifique se ela retorna os resultados esperados
    result = get_config()
    
    # Adicione suas asserções aqui com base no que você espera
    assert 'feature1' in result['features_configs']
    assert 'feature2' in result['features_configs']
    assert result['model_configs']['algorithm'] == 'RandomForest'
    assert result['model_configs']['parameters']['n_estimators'] == 100

    # Limpeza: Remova o arquivo de teste
    os.remove('src/yamls/test_config.yaml')
