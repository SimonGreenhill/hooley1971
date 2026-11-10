def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_counts(cldf_dataset):
    assert len(list(cldf_dataset["LanguageTable"])) == 55
    assert len(list(cldf_dataset["ParameterTable"])) == 128
    assert len(list(cldf_dataset["FormTable"])) == 6716
    assert len(list(cldf_dataset["CognateTable"])) == 6716


def test_barred_g(cldf_dataset):
    forms = {(f["Language_ID"], f["Parameter_ID"]): f for f in cldf_dataset["FormTable"]}
    assert forms[("Mapos", "17_lie")]["Form"] == "ǥep"
