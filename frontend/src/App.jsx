import { useEffect, useState } from "react"
import { TodoForm } from "./TodoForm"
import "./styles.css"
import { TodoList } from "./TodoList"

export default function App() {
  const [todos, setTodos] = useState([])
  
  useEffect(() => {
    fetch("http://localhost:8000/todo")
    .then(response => response.json())
    .then(data => setTodos(data.data))
  }, []) 


  const fetchTodos = async () => {
    const response = await fetch("http://localhost:8000/todo")
    const data = await response.json()
    setTodos(data.data)
  }
  
  async function addTodo(title) {
    fetch('http://localhost:8000/todo', {
    method: 'POST',
    headers: {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    },
    
      body: JSON.stringify({
        'item': title,
        'completed': false
      })
    })

    await fetchTodos()
  }

  async function deleteTodo(id) {
    await fetch('http://localhost:8000/todo/?item_id='+id, {
      method: 'DELETE',
      headers: {
        'accept': 'application/json'
      }
    })

    await fetchTodos()
  }

  async function toggleTodo(id, completed) {
    let url = 'http://localhost:8000/todo/' + id + '' + '?completed=';

    if(completed){
      url += true
    } else {
      url += false
    }

    await fetch(url, {
      headers: {
          'accept': 'application/json'
      }
    })

    await fetchTodos()
  }

  return (
    <>
      <div class='item-entry'>
        <TodoForm onSubmit={addTodo} />
      </div>

      <div class='grocery-list'>
        <TodoList todos={todos} toggleTodo={toggleTodo} deleteTodo={deleteTodo} />
      </div>
    </>
  )
}