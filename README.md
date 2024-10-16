# INF1407-T1
# Arthur Xavier Tavares - 1921023

## Escopo do Site

O site desenvolvido é uma plataforma de reviews de jogos, onde os usuários podem criar, editar, visualizar e deletar reviews de diversos jogos. O site possui funcionalidades de autenticação, permitindo que os usuários se registrem, façam login, atualizem seus dados e alterem suas senhas.

## Funcionalidades do Site

1. **Página Inicial**: Caso o usuário esteja logado, exibe uma lista de todas as reviews cadastradas, com opções para editar ou deletar cada review. Caso seja o usuário não esteja logado, exibe a página de Login.
2. **Criação de Review**: Usuários autenticados podem criar novas reviews preenchendo um formulário.
3. **Edição de Review**: Usuários podem editar reviews existentes.
4. **Deleção de Review**: Usuários podem deletar reviews existentes.
5. **Autenticação de Usuário**:
    - Registro de novos usuários.
    - Login de usuários existentes.
    - Atualização de dados do usuário.
    - Alteração de senha.
6. **Templates**: O site utiliza templates do Django para renderizar as páginas HTML, garantindo uma interface consistente e fácil de navegar.

## Estrutura do Projeto

- `src/Reviews/ReviewApp/models.py`: Define o modelo `Review` utilizado no banco de dados.
- `src/Reviews/ReviewApp/templates/`: Contém os templates HTML utilizados para renderizar as páginas do site.
    - `base.html`: Template base utilizado por todas as outras páginas.
    - `lista_review.html`: Lista todas as reviews cadastradas.
    - `cria_review.html`: Formulário para criação de uma nova review.
    - `atualiza_review.html`: Formulário para atualização de uma review existente.
    - `deleta_review.html`: Confirmação de deleção de uma review.
    - `registration/`: Contém templates relacionados à autenticação de usuário (login, registro, alteração de senha, etc.).



## Considerações Finais

Este projeto foi desenvolvido como parte da disciplina INF1407, com o objetivo de aplicar os conhecimentos adquiridos sobre desenvolvimento web utilizando o framework Django.