from src.fun import add,sub

def test_add():
    assert add(5,6)==11
    assert add(1,6)==7
    assert add(-1,6)==5
    
def test_sub():
    assert sub(5,6)==-1
    assert sub(1,6)==-5
    assert sub(-1,6)==-7