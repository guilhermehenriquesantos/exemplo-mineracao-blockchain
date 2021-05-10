from hashlib import sha256
import time

MAX_NONCE = 100000000000


def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print('___________________________________')
            print(f'\nBitcoins extraídos com sucesso!\n\nValor encontrado para nonce: {nonce}')
            print('___________________________________')
            return new_hash
    
    raise BaseException('Não foi possível realizar a mineração com, tentamos {MAX_NONCE} vezes')


if __name__=='__main__':
    transactions='''
        Dhaval->Bhavin->20,
        Mando->Cara->45
    '''
    difficulty = 4
    previous_hash = '0000000c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78'

    start = time.time()

    print('\n#######################')
    print('# Iniciando mineração #')
    print('#######################\n')

    new_hash = mine(5, transactions, previous_hash, difficulty)
    
    total_time = str((time.time() - start))
    
    print('\n#################')
    print('# Fim mineração #')
    print('#################\n')

    print(f'Tempo decorrido: {total_time} segundos\n')

    print('_________________________________________________________________________________')

    print(f'\nHash anterior: {previous_hash}\n')

    print('____________________________________________________________________________________________________________________')
    
    print(f'\n---> O novo hash gerado após a mineração é: {new_hash} <---')

    print('____________________________________________________________________________________________________________________\n')