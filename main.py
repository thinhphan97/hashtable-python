import time

from hashtable import HashTable


def main():
    
    hash_table = HashTable(50)

    print(hash_table.get_size())
    # insert some values
    hash_table.set_val('gfg@example.com', {"id":10, "gmail":"gfg@example.com"})
    time.sleep(4)
    print(hash_table.get_size())
    hash_table.set_val('portal@example.com', {"id":3, "gmail":"portal@example.com"})
    print(hash_table.get_size())
    time.sleep(10)
    print(hash_table.get_size())
    print(hash_table)
    print()

    hash_table_copy = HashTable()
    hash_table_copy.set_val('portal@example.com', {"id":4, "gmail":"portal@example.com"})
    print(hash_table_copy)
    print()
    print(hash_table)
    print()
    print(hash_table_copy)

    # search/access a record with key
    print(hash_table.get_val('portal@example.com'))
    print()
    time.sleep(2)
    print(hash_table)
    print()
    time.sleep(2)
    print(hash_table)
    print()

if __name__ == "__main__":
    main()
    