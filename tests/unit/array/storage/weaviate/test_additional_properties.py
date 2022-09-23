from docarray import Document, DocumentArray


def test_get_additional(start_storage):
    da = DocumentArray(
        storage="weaviate", config={"name": "Test", "host": "localhost", "port": 8080}
    )

    with da:
        da.extend(
            [
                Document(text="r0", embedding=[0, 0, 0]),
                Document(text="r2", embedding=[2, 2, 2]),
                Document(text="r4", embedding=[4, 4, 4]),
                Document(text="r5", embedding=[2, 2, 2]),
                Document(text="r6", embedding=[4, 4, 4]),
            ]
        )

    additional = ["creationTimeUnix", "lastUpdateTimeUnix"]
    results = da.find(
        DocumentArray([Document(text="r5", embedding=[2, 2, 2])]),
        limit=1,
        additional=additional,
    )

    for res in results:
        assert res[:, "tags__creationTimeUnix"][0] is not None
        assert res[:, "tags__lastUpdateTimeUnix"][0] is not None
