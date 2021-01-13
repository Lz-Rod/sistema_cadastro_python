# Sistema de cadastro de usuário
## Codificado em Python e SQL
Sistema de cadastro simples CRUD integrado totalmente com SQL Server

### Telas do sistema
![print_menu](https://github.com/Lz-Rod/sistema_cadastro_python/blob/main/docs/img_readme/menu_principal.PNG)
- Menu principal: Nessa tela é possivel escolher entre as opções: Criar, Ver, Atualizar, Deletar e Sair do sistema.

![print_menu](https://github.com/Lz-Rod/sistema_cadastro_python/blob/main/docs/img_readme/criar_cadastro.PNG)
- Criar cadastro: Nessa tela o usuário é guiado a preenchar cada informação para o novo cadastro, e ao fim o cadastro é salvo e é perguntado se deseja criar outro novo cadastro.

![print_menu](https://github.com/Lz-Rod/sistema_cadastro_python/blob/main/docs/img_readme/ver_cadastros.PNG)
- ver cadastros: Nessa tela é realizada uma busca no database através no ID, nome ou país de residencia do cadastro. No caso do ID é retornado somente os dados respectivos a ele e no caso do nome ou país de residência é retornado o numero de cadastros respectivos aquele parãmetro e uma lista com os mesmos.

![print_menu](https://github.com/Lz-Rod/sistema_cadastro_python/blob/main/docs/img_readme/atualizar_cadastro.PNG)
- Atualizar cadastro: Nessa tela é solicitado o ID que será alterado, e após mostrar o cadastro é retornado uma lista com as opções que podem ser alteradas. Ao fim é perguntado se deseja alterar algo mais naquele cadastro ou outro cadastro.

![print_menu](https://github.com/Lz-Rod/sistema_cadastro_python/blob/main/docs/img_readme/excluir_cadastro.PNG)
- Excluir cadastro: Nessa tela é solicitado o ID que deseja excluir, ao preenchê-lo nos retorna os dados do cadastro e pede a confirmação para exclusão, em caso positivo o sistema retorna cadastro excluído com sucesso e pergunta se deseja excluir outro cadastro.

### Mais informações:
- Sistema criado em Python 3.9;
- usadas bibliotecas externas: time e pyodbc;
- Criado pacotes e módulos internos para organização do código;
- Feito tratamento de erros interno do Python;
- Adicionado cores no terminal do sistema;
- Usado SQL e SQL server para compor o database a qual se conecta o sistema.
