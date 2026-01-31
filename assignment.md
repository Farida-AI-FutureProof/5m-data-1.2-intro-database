# Assignment

## Brief

Create an ERD for each of the following case study question.

## Instructions

Paste the answer as DBML in the answer code section below each question.

### Question 1

Construct an ERD for a social media company whose database includes information about users, their followers, and the posts that they make. Users can follow multiple users and create multiple posts.

Each entity has the following attributes:

- User: id, username, email, created_at
- Post: id, title, body, user_id, status, created_at
- Follows: following_user_id, followed_user_id, created_at

Answer:

```dbml
Table users {
  id int [pk, increment]
  username varchar [not null, unique]
  email varchar [not null, unique]
  created_at timestamp [not null]
}

Table posts {
  id int [pk, increment]
  title varchar [not null]
  body text [not null]
  user_id int [not null]
  status varchar [not null] // e.g., draft, published, archived
  created_at timestamp [not null]
}

Table follows {
  following_user_id int [not null]
  followed_user_id int [not null]
  created_at timestamp [not null]

  Indexes {
    (following_user_id, followed_user_id) [pk]
  }
}

Ref: posts.user_id > users.id
Ref: follows.following_user_id > users.id
Ref: follows.followed_user_id > users.id



### Question 2

Construct an ERD for a company that sells books online. The company has a website where customers can browse available books and add them to their shopping carts. Each cart can contain multiple books.

There are 4 entities, think of what attributes each entity should have.

- Customer
- Book
- Cart
- CartItem

Answer:

Table customers {
  id int [pk, increment]
  name varchar [not null]
  email varchar [not null, unique]
  created_at timestamp [not null]
}

Table books {
  id int [pk, increment]
  title varchar [not null]
  author varchar [not null]
  isbn varchar [unique]
  price decimal(10,2) [not null]
  stock_qty int [not null, default: 0]
  created_at timestamp [not null]
}

Table carts {
  id int [pk, increment]
  customer_id int [not null]
  status varchar [not null] // e.g., active, checked_out, abandoned
  created_at timestamp [not null]
}

Table cart_items {
  id int [pk, increment]
  cart_id int [not null]
  book_id int [not null]
  quantity int [not null, default: 1]
  unit_price decimal(10,2) [not null] // price at time of adding to cart
  created_at timestamp [not null]

  Indexes {
    (cart_id, book_id) [unique]
  }
}

Ref: carts.customer_id > customers.id
Ref: cart_items.cart_id > carts.id
Ref: cart_items.book_id > books.id
