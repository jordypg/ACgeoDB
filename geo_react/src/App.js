import React, {useState, useEffect} from 'react';
import axios from "axios";
import logo from './logo.svg';
import './App.css';
import { render } from '@testing-library/react';

function removePreviousResults(){
  let previousResults = document.getElementById("search_results");
  if(previousResults != null){
    previousResults.remove();
  }
}

function SearchField({number}){
  const selectId = "fieldSelect" + number;
  const textId = "fieldValue" + number;
  return (
    <>
      <select name={selectId} id={selectId}>
        <option value="progName">Program name</option>
        <option value="progCountry">Country</option>
        <option value="decFact">Deciding Factor for Program</option>
        <option value="primLang">Primary Language Spoken</option>
        <option value="estCost">Estimated Cost Spent</option>
        <option value="primLang">Extracurricular Activities</option>
        <option value="primLang">Recommendation Rating</option>
        <option value="primReas">Primary Reason for Study Abroad</option>
        <option value="partMajor">Major</option>
      </select>
      <input id={textId} type="text"/> <br></br>
    </>
  );
}

function AddFieldsButton({handleClick}) {
  
  removePreviousResults();
  return (
    <button onClick={handleClick}>
      Add field
    </button>
  );
}

function SearchButton({handleClick, values}){
  return (
    <button onClick={handleClick}>
      Search
    </button>
  )
}



function QueryResults({entries}){
  const [columnHeaders, setColumnHeaders] = useState(["Program name", "Country", "Deciding Factor for Program", "Primary Language Spoken", "Estimated Cost Spent", "Extracurricular Activities", "Recommendation Rating", "Primary Reason for Study Abroad", "Major"]);
  let rows = [];

  //Add column headers to table
  let headerCell = [];
  for(var i = 0; i < columnHeaders.length; i++){
    let cellID = `header${i}`;
    headerCell.push(<td key={cellID} id={cellID}>{columnHeaders[i]}</td>)
  }
  rows.push(<tr key="header" id="header">{headerCell}</tr>)

  //Add rows from entries
  for (var i = 0; i < entries.length; i++){
    let rowID = `data_row${i}`
    let cell = []
    for (var idx = 0; idx < entries[i].length; idx++){
      let cellID = `data_cell${i}-${idx}`
      cell.push(<td key={cellID} id={cellID}>{entries[i][idx]}</td>)
    }
    rows.push(<tr key={i} id={rowID}>{cell}</tr>)
  }
  return(
    <div className="container">
      <div className="row">
        <div className="col s12 board">
          <table id="search_results">
              <tbody>
                {rows}
              </tbody>
            </table>
        </div>
      </div>
    </div>
  )
    
}

function App() {

  const [searchFields, setSearchFields] = useState(1)
  let test = [["AAA", "BBB", "CCC"], ["DDD", "EEE", "FFF"], ["GGG", "HHH", "III"]]
  function handleAddFieldsButtonClick() {
    setSearchFields(searchFields + 1)
    render(<SearchField number={searchFields}/>);
  }

  function handleSearchButtonClick(){
    removePreviousResults();


    fetch("/test_student")
      .then(response => response.json())
      .then(data => console.log(data))


            

    render (<QueryResults entries = {test}/>)
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

