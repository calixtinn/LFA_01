"""
*************************************************************************************************
*                   Trabalho 01 - Linguagens Formais e Autômatos Finitos                        *
*                                                                                               *
*   @teacher: Walace Rodrigues                                                                  *
*   @author: Matheus Calixto - ⁠⁠⁠0011233                                                          *
*   @author: Samuel Terra    - 0011946                                                          *
*   @lastUpdate: 25/05/2017                                                                     *
*                                                                                               *
*************************************************************************************************
"""

from Controller.AFDController import AFDController
from View.AFDView import AFDView

"""
*************************************************************************************************
*   A aplicação deve ser executada usado Python 3                                               *
*   Para realizar a execução, basta usar o seguite comando:                                     *
*                                                                                               *
*   $ python3 main.py                                                                           *       
*                                                                                               *
*   Caso não possua a versão necessária instalada, ela pode ser instalada da seguinte forma:    *
*                                                                                               *
*   $ sudo apt-get update                                                                       *
*   $ sudo apt-get -y upgrade                                                                   *
*   $ sudo apt-get install -y python3-pip                                                       *
*   $ sudo apt-get install build-essential libssl-dev libffi-dev python-dev                     *
*   $ sudo apt-get install -y python3-venv                                                      *
*                                                                                               *
*   Aplicação também faz uso de bibliotecas que podem não estarem instaladas em sistema         *
*   operacional. As bibliotecas são:                                                            *
*   - TkInter                                                                                   *
*   - ElementTree                                                                               *
*   - Minidom                                                                                   *
*                                                                                               *
*   Caso alguma não esteja instalada, siga o precesso abaixo:                                   *
*                                                                                               *
*   Instalar biblioteca TkInter:                                                                *
*                                                                                               *
*   $ sudo apt-get install python python-tk idle python-pmw python-imaging                      *
*                                                                                               *
*   A biblioteca Minidom já vem no pacote do Python, caso apresente problemas, tente reinstalar *
*   o python                                                                                    *
*                                                                                               *
*   Instalar a biblioteca para realizar parser usando ElementTree                               *
*                                                                                               *
*   $ sudo apt-get install python-lxml                                                          *
*                                                                                               *
*                                                                                               *
*************************************************************************************************
"""
if __name__ == '__main__':
    AF = AFDController()
    view = AFDView()
    view.menuPrincipal()
