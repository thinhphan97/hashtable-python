from hashtable import HashTable
import time


def main():
    
    hash_table = HashTable(50)

    # insert some values
    hash_table.set_val('gfg@example.com', {"id":10, "gmail":"gfg@example.com"}, ttl=2)
    time.sleep(4)
    hash_table.set_val('portal@example.com', {"id":3, "gmail":"portal@example.com"})

    print(hash_table)
    print()

    hash_table_copy = HashTable()
    hash_table_copy.set_val('portal@example.com', {"id":4, "gmail":"portal@example.com"})
    print(hash_table_copy)
    print()
    print(hash_table)
    print()
    print(hash_table_copy)
    print()
    print(hash_table)
    print()
    # search/access a record with key
    print(hash_table.get_val('portal@example.com'))
    print()
    time.sleep(2)
    print(hash_table)
    print()
    time.sleep(2)
    print(hash_table)
    print()
    time.sleep(2)
    print(hash_table)
    print()
    time.sleep(2)
    print(hash_table)
    print()
    time.sleep(2)
    print(hash_table)
    print()
if __name__ == "__main__":
    main()
    