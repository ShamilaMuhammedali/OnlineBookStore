import React, { useState, useEffect } from 'react'
import axios from 'axios'
import './BookListPage.css'
import { Link } from 'react-router-dom'

const BookListPage = () => {
  const [books, setBooks] = useState([])
  const [genres, setGenres] = useState([])
  const [selectedGenre, setSelectedGenre] = useState('')

  useEffect(() => {
    fetchData()
  }, [])

  const fetchData = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/User/search/')
      setBooks(response.data)
      const uniqueGenres = Array.from(
        new Set(response.data.map((book) => book.book_genre))
      )
      setGenres(uniqueGenres)
    } catch (error) {
      console.error('Error fetching data:', error)
    }
  }

  const handleGenreChange = (event) => {
    setSelectedGenre(event.target.value)
  }

  const addToCart = async (bookId) => {
    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/User/addtocart/${bookId}`
      )
      alert('Book added to cart successfully!');
    } catch (error) {
      console.error('Error adding to cart:', error)
    }
  }

  return (
    <div className="book-container">
      {/* Navigation bar */}
      <nav className="navigation-bar">
        <ul>
          <li>
            <Link to="/search">Search</Link>
          </li>
          <li>
            <Link to="/cart">Cart</Link>
          </li>
          <li>
            <Link to="/orderlist">Order List</Link>
          </li>
          <li>
            <Link to="/logout">Logout</Link>
          </li>
        </ul>
      </nav>

      {/* Filter by Genre */}
      <div className="genre-filter">
        <select value={selectedGenre} onChange={handleGenreChange}>
          <option value="">All Genres</option>
          {genres.map((genre) => (
            <option key={genre} value={genre}>
              {genre}
            </option>
          ))}
        </select>
      </div>

      {/* Book list */}
      <div className="book-list">
        <h1>
          <center>Book List</center>
        </h1>
        <div className="book-cards">
          {books
            .filter(
              (book) =>
                selectedGenre === '' || book.book_genre === selectedGenre
            )
            .map((book) => (
              <div key={book.id} className="book-card">
                <h3>{book.book_title}</h3>
                <img
                  className="book-image"
                  src={`http://127.0.0.1:8000${book.book_coverpage}`}
                  alt={book.book_title}
                />
                <p>
                  <strong>Author:</strong> {book.book_author}
                </p>
                <p>
                  <strong>Genre:</strong> {book.book_genre}
                </p>
                <p>
                  <strong>Price:</strong> {book.book_price}
                </p>
                <button
                  className="add-to-cart-button"
                  onClick={() => addToCart(book.id)}
                >
                  Add to Cart
                </button>
              </div>
            ))}
        </div>
      </div>
    </div>
  )
}

export default BookListPage
