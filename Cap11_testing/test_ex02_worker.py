# %%
from ex02_worker import Worker
import pytest
# %%

@pytest.fixture

def get_worker():
    john = Worker('john','obama',36000)
    return john
    
def test_worker(get_worker):
    assert get_worker.first_name == 'John'
    assert get_worker.last_name == 'Obama'
    
def test_default_raise(get_worker):
    get_worker.increasce_salary()
    assert get_worker.salary == 41000
    
def test_default_raise(get_worker):
    get_worker.increasce_salary(10000)
    assert get_worker.salary == 46000