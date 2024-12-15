# Criptografia em Python


Este repositório compila códigos e exemplos práticos de **criptografia** implementados em **Python**. O projeto abrange conceitos fundamentais e práticas de criptografia simétrica, assimétrica e hashing.

## 🔧 Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:**
  - `cryptography`
  - `PyCryptodome`

---

## 🔍 Conteúdo do Repositório

| Pasta/Arquivo     | Descrição                                                                 |
|-------------------|------------------------------------------------------------------------------|
| `PrimeiraAula`    | Introdução à criptografia: conceitos iniciais e códigos básicos.         |
| `SegundaAula`     | Criptografia simétrica usando AES (modo ECB e CBC).                         |
| `TerceiraAula`    | Criptografia assimétrica com RSA: geração de chaves e encriptação.        |
| `QuartaAula`      | Hashing e verificação de integridade usando SHA-256.                       |
| `QuintaAula`      | Uso prático: assinaturas digitais.                                          |
| `SextaAula`       | Exercícios finais: combinação de métodos criptográficos.                  |
| `chave_privada.pem` | Exemplo de chave privada gerada.                                           |
| `chave_publica.pem` | Exemplo de chave pública gerada.                                           |

---

## 🛠️ Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Gabrieel-Lopees/PythonCrypto.git
   cd PythonCrypto
   ```

2. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   
   pip install -r requirements.txt
   ```

---

## 🔑 Exemplos de Uso

### Criptografia Simétrica com AES
```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Geração de chave e inicialização
key = get_random_bytes(16)  # Chave de 16 bytes
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce

# Encripta mensagem
ciphertext, tag = cipher.encrypt_and_digest(b"Mensagem secreta")
print("Texto cifrado:", ciphertext)
```

### Criptografia Assimétrica com RSA
```python
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gerar chave privada
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Serializar chave privada
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.BestAvailableEncryption(b"senha-secreta")
)
with open("private_key.pem", "wb") as f:
    f.write(pem)
```

---

## 📖 Referências
- [Documentação Cryptography](https://cryptography.io/)
- [PyCryptodome](https://www.pycryptodome.org/)
- [Conceitos de RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

---

## 🌟 Objetivo
Este projeto serve como uma base de aprendizado e referência para aplicações de criptografia em Python, podendo ser expandido para soluções mais avançadas.

---

## 💍 Autor
Desenvolvido por **Gabriel de Andrade Lopes** durante o segundo semestre de 2024.

---

## Licença

Este projeto é licenciado sob os termos da licença da Universidade Federal de Santa Maria.
