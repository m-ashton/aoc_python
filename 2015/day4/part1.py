from hashlib import md5

def main():
    with open('./input.txt', 'r') as secret_key_file:
        secret_key = secret_key_file.read().strip()
        md5_hash = ''

        i = -1
        while not md5_hash.startswith('00000'):
            i += 1
            md5_hash = md5(bytes(secret_key + str(i), 'utf-8')).hexdigest()
        print(f"{i} produces {md5_hash}")

if __name__ == '__main__':
    main()
