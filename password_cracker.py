import hashlib

def crack_sha1_hash(hash, use_salts=False):
    passwords_arr = []
    read_and_add_to_arr("top-10000-passwords.txt", passwords_arr)

    if use_salts:
        top_salts_passwords = {}
        top_salts = []
        read_and_add_to_arr("known-salts.txt", top_salts)
        for bsalt in top_salts:
            for bpassword in passwords_arr:
                prepended = hashlib.sha1(bsalt.encode() + bpassword.encode()).hexdigest()
                appended = hashlib.sha1(bpassword.encode() + bsalt.encode()).hexdigest()
                top_salts_passwords[prepended] = bpassword
                top_salts_passwords[appended] = bpassword
        if hash in top_salts_passwords:
            return top_salts_passwords[hash]

    passwords_dict = {}
    for p in passwords_arr:
        hash_line = hashlib.sha1(p.encode()).hexdigest()
        passwords_dict[hash_line] = p

    if hash in passwords_dict:
        return passwords_dict[hash]

    return "PASSWORD NOT IN DATABASE"

def read_and_add_to_arr(file_name, arr):
    with open(file_name, "r") as f:
        for line in f:
            arr.append(line.strip())
