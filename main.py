from hashtable import HashTable
import time
import json

def main():
    hash_table = HashTable(50)

    # insert some values
    hash_table.set_val('gfg@example.com', {"id":10, "gmail":"gfg@example.com"})
    hash_table.set_val('portal@example.com', {"id":3, "gmail":"gfg@example.com"})

    print(hash_table)
    print()

    hash_table_copy = HashTable(100)
    hash_table_copy.set_val('portal@example.com', {"id":4, "gmail":"gfg@example.com"})
    print(hash_table_copy)
    print()
    print(hash_table)
    time.sleep(10)
    print(hash_table_copy)
    print()
    print(hash_table)
    # search/access a record with key
    print(hash_table.get_val('portal@example.com'))
    print()
    time.sleep(2)
    print(hash_table)
    time.sleep(2)
    print(hash_table)
    time.sleep(2)
    print(hash_table)

if __name__ == "__main__":
    main()