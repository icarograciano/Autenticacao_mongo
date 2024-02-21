# Sistema de Autenticação com Flask, Bootstrap e MongoDB

Este projeto foi desenvolvido como parte de um trabalho acadêmico, focando na exploração de conceitos essenciais de segurança web, incluindo autenticação, autorização e criptografia. 
Utilizando as tecnologias Flask, Bootstrap e MongoDB, o sistema oferece uma base básica para entender e implementar práticas de segurança em aplicações web.

## Funcionalidades Principais

- **Autenticação Segura:** Utilizando o Flask-Bcrypt, as senhas dos usuários são armazenadas de forma segura no banco de dados, garantindo a proteção contra ameaças de segurança.
- **Controle de Acesso:** Implementação de um sistema de controle de acesso, permitindo que usuários autenticados acessem recursos específicos, enquanto mantêm outros protegidos.
- **Persistência de Dados:** Utilização do MongoDB para armazenar dados dos usuários de maneira eficiente e escalável.

## Pré-requisitos
Antes de começar, certifique-se de ter o Python, Flask, Bootstrap e MongoDB instalados em seu ambiente de desenvolvimento.

# Instalação
1. Clone o repositório:
    ```
    git clone https://github.com/seu-nome-de-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
2. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
3. Execute o script de preparação do banco de dados:
    ```
    python prepara_banco.py
    ```

## Uso
1. Inicie a aplicação Flask:
    ```
    python app.py
    ```
2. Abra seu navegador da web e vá para [http://localhost:5000](http://localhost:5000)

Explore e experimente as funcionalidades de autenticação, autorização e criptografia implementadas neste projeto.

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões, relatórios de bugs ou contribuições, siga estas etapas:
1. Fork o projeto
2. Crie um novo branch (`git checkout -b feature/nome-da-sua-feature`)
3. Faça alterações e as commit (`git commit -am 'Adicione sua feature'`)
4. Faça push para o branch (`git push origin feature/nome-da-sua-feature`)
5. Abra um pull request

## Licença
Este projeto é livre e pode ser utilizado por qualquer pessoa sem restrições específicas. Sinta-se à vontade para explorar, modificar e distribuir o código.

## Autor
Este projeto foi desenvolvido por Icaro Graciano. Qualquer dúvida, abra uma issues.
