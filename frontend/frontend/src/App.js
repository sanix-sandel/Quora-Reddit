import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import NavBar from './components/Navbar.js';
import SideBarL from './components/SidebarL.js';
import SideBarR from './components/SidebarR.js';
import Body from './components/body.js';

import Websocket from 'react-websocket';
import  fetchquestions from './api';


class App extends Component{

    constructor(props){
      super(props);
      this.state={
        questions:[]
      }
      this.getData=this.getData.bind(this);
    }  

    componentDidMount(){
      this.getData();
    }

    async getData(){
      let data=await fetchquestions();
      console.log(data);
      this.setState({questions:data})
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
                <Body key={q.id} quest={q}/>
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
