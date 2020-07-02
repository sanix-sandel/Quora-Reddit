import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import NavBar from './components/Navbar.js';
import SideBarL from './components/SidebarL.js';
import SideBarR from './components/SidebarR.js';
import Body from './components/body.js';


class App extends Component{

    state={
      questions:[
        {id:0, texte:"Is life unfair ?"},
        {id:1, texte:"Is easy to live in Africa ?"},
        {id:2, texte:"Proghramming is tough ?"},
        {id:3, texte:"What does it mean ?"},
      ]
    }

  render(){
    return (
      <div>
        <nav className="navbar navbar-expand-lg navbar-light fixed-top">
          <NavBar/>
        </nav>
        <div class="container-fluid">
          <div class="row">
            <SideBarL/>
            <div class="col-lg-7">
              {this.state.questions.map(q=>
                <Body/>
              )}
            </div>
            <SideBarR/>
          </div>  
        </div>
      </div>
    );
  }
  
}

export default App;
