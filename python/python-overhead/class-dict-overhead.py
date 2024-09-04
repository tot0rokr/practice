import timeit

NUM_INSTANCES = 2000

class FeatureSet:
    def __init__(
            self, user_id, **kwargs,
    ):
        self.user_id = user_id
        for k, v in kwargs.items():
            setattr(self, k, v)

def create_class_instances() -> None:
    for i in range(NUM_INSTANCES):
        obj = FeatureSet(
            user_id=i,
            **{"feature"+str(j): i * j for j in range(30)}
        )

def create_dicts() -> None:
    for i in range(NUM_INSTANCES):
        obj = {
            "user_id": i,
            **{"feature"+str(j): i * j  for j in range(30)}
        }

class_time = timeit.timeit(create_class_instances, number=1)
print(f"class: {class_time * 1000:.1f}ms")

dict_time = timeit.timeit(create_dicts, number=1)
print(f"dict: {dict_time * 1000:.1f}ms")
