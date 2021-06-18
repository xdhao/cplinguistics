#encoding "utf8"
PolitName -> Word<kwtype=politiki> | Word<kwtype=dostopr>;

Polit -> PolitName interp (Polit.Surname);

