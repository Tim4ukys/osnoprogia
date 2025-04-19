import hashtable as ht

dick = ht.ht_init(100)
ht.ht_set(dick, "Vasia", "333-45-67")
ht.ht_set(dick, "Police", "02")

assert ht.ht_get(dick, "Police") == "02"
