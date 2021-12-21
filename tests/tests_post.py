
from pydantic.types import T, Json
from app import schemas
import pytest


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")

    def validate(post):
        return schemas.PostOut(**post)
    
    post_map = map(validate, res.json())
    post_list = list(post_map)
 
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    assert post_list[0].Post.id == test_posts[0].id

def test_unauthorized_user_get_all_posts(client, test_posts):

    res = client.get("/posts/")
    assert res.status_code == 401

def test_unauthorized_user_get_one_posts(client, test_posts):

    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):

    res = authorized_client.get(f'/posts/8888')
    assert res.status_code == 404

def test_get_one_posts(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    
    post = schemas.PostOut(**res.json())

    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content


@pytest.mark.parametrize("title, content, published", [
    ("awesome title", "awesome_content", True),
    ("2nd awesome title", "2nd awesome_content", True),
    ("3rd awesome title", "3rd awesome_content", False),
    ("3rd awesome title", "3rd awesome_content", True),
    ("4th awesome title", "4th awesome_content", False),
    
])
def test_create_posts(authorized_client, test_posts, test_user, title, content, published):
    
    res = authorized_client.post("/posts/", json={"title":title, "content":content, "published":published})
    
    created_post = schemas.PostResponse(**res.json())

    assert res.status_code == 201
    assert created_post.published == published
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.owner.id == test_user["id"]

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post('/posts/', json={"title":"Some title", "content":"Some content"})
    
    created_post = schemas.PostResponse(**res.json())

    assert res.status_code == 201
    assert created_post.published == True
    assert created_post.title == "Some title"
    assert  created_post.content == "Some content"
    assert created_post.owner.id == test_user["id"]

def test_unauthorized_user_create_post(client, test_posts, test_user):
    res = client.post('/posts/', json={"title":"Some title", "content":"Some content"})
    
    assert res.status_code == 401


def test_unauthorized_delete_post(client, test_posts, test_user):

    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_success_delete_posts(authorized_client, test_posts, test_user):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")

    assert res.status_code == 204

def test_delete_not_found(authorized_client, test_posts, test_user):
    res = authorized_client.delete(f"/posts/{8000}")

    assert res.status_code == 404

def test_delete_other_user_post(authorized_client, test_posts, test_user):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")

    assert res.status_code == 403

def test_update_post(authorized_client, test_posts, test_user):
    data = {
        "title":"updated title",
        "content":"updated",
        "id":test_posts[0].id
    }
    
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)

    updated_post = schemas.PostResponse(**res.json())

    assert res.status_code == 200
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]

def test_update_other_owners_posts(authorized_client, test_posts, test_user, test_user2):
    data = {
        "title":"updated title",
        "content":"updated",
        "id":test_posts[0].id
    }
    
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code == 403  

def test_unauthorized_user_update_post(client, test_posts, test_user, test_user2):
    
    data = {
        "title":"updated title",
        "content":"updated",
        "id":test_posts[0].id
    }

    res = client.put(f"/posts/{test_posts[0].id}", json=data)
    assert res.status_code == 401

def test_update_post_not_found(authorized_client, test_posts, test_user):
    data = {
        "title":"updated title",
        "content":"updated",
        "id":test_posts[0].id
    }
    
    res = authorized_client.put(f"/posts/{8000}", json=data)

    assert res.status_code == 404