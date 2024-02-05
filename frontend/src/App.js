import React from 'react'
import UserAuthPage from './UserAuth/UserAuthPage'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import BookListPage from './Book/BookListPage'

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<UserAuthPage/>} />
        <Route path='/booklist' element={<BookListPage/>} />
      </Routes>
    </BrowserRouter>
  )
}
