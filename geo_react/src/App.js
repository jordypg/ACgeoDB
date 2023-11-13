import React, {useState} from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import { render } from '@testing-library/react';

function SearchField({number}){
  const selectId = "fieldSelect" + number;
  const textId = "fieldValue" + number;
  return (
    <>
      <select name={selectId} id={selectId}>
        <option value="progName">Program name</option>
        <option value="country">Country</option>
        <option value="partMajor">Participant major</option>
      </select>
      <input id={textId} type="text"/> <br></br>
    </>
  );
}

function AddFieldsButton({handleClick}) {
  

  return (
    <button onClick={handleClick}>
      Add field
    </button>
  );
}

function SearchButton({handleClick, values}){
  return (
    <button onclick={handleClick}>
      Search
    </button>
  )
}

function QueryResults({entries}){
  const [columnHeaders, setColumnHeaders] = useState([])
  const [results, setResults] = useState([])

}

function App() {

  const [searchFields, setSearchFields] = useState(1)

  function handleAddFieldsButtonClick() {
    setSearchFields(searchFields + 1)
    render(<SearchField number={searchFields}/>);
  }

  function handleSearchButtonClick(){

  }

  return (
    <>
    <h1>GEODB Query Prototype</h1>
    <AddFieldsButton handleClick={handleAddFieldsButtonClick}/>
    <SearchButton handleClick={handleSearchButtonClick}/>
    <br></br>
    <SearchField number={searchFields}/>
      
    </>
  );
}

export default App;

