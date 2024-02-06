from dataclasses import dataclass
import timeit
from typing import List

from pydantic import BaseModel
import gc

class FeatureSetPydantic(BaseModel):
    user_id: int
    features: List[float]

def create_pydantic_instances() -> None:
    for i in range(4000):
        obj = FeatureSetPydantic(
            user_id=i,
            features=[1.0 * i + j for j in range(50)],
        )

elapsed_time = timeit.timeit(create_pydantic_instances, number=1)
print(f"pydantic: {elapsed_time * 1000:.2f}ms")


gc.collect()

class FeatureSet:
    def __init__(self, user_id: int, features: List[float]) -> None:
        self.user_id = user_id
        self.features = features

def create_class_instances() -> None:
    for i in range(4000):
        obj = FeatureSet(
            user_id=i,
            features=[1.0 * i + j for j in range(50)],
        )

elapsed_time = timeit.timeit(create_class_instances, number=1)
print(f"class: {elapsed_time * 1000:.2f}ms")


gc.collect()

@dataclass
class FeatureSetDataclass:
    user_id: int
    features: List[float]

def create_class_instances() -> None:
    for i in range(4000):
        obj = FeatureSetDataclass(
            user_id=i,
            features=[1.0 * i + j for j in range(50)],
        )

elapsed_time = timeit.timeit(create_class_instances, number=1)
print(f"dataclass: {elapsed_time * 1000:.2f}ms")
