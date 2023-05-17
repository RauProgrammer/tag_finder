# Projeto desenvolvido para identificar o tipo de serviço de garantia de máquinas Dell
> O código que consta nesse repositório foi desenvolvido especificamente para auxiliar na busca e identificação de serviços de garantia para mais de 1800 máquinas da Dell, adquiridas pela Secretaria Estadual da Saúde.

_O processo é realizado na seguinte ordem:_
- O código é alimentado por uma planilha com dois campos: "TAGS" e "SERVIÇOS"
- Transformar a planilha em um dicionário
- Repetir os passos abaixo para a **quantidade de TAGS** da planilha
	- Entrar no site de suporte da Dell: [Suporte Dell](https://www.dell.com/support/home/pt-br)
	- Localizar a máquina através da TAG
	- Exibir os detalhes da máquina
	- Verificar qual o tipo de serviço
	- Salvar em uma váriavel o texto
	- Atualizar o dicionário com o tipo de serviço
- Transformar o dicionário em um dataframe
- Gerar uma nova planilha com o dataframe atualizado

### **_by Raul Nunes_**
