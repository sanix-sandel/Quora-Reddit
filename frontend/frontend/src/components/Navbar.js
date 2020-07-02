import React, {Component} from 'react';

class NavBar extends Component{
    render(){
        return(
        
            <div className="container-fluid">
               <a className="navbar-brand mylogo" href="#"></a>
               <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
               <span className="navbar-toggler-icon"></span>
               </button>
               <div className="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul className="navbar-nav mr-auto">
                     <li className="nav-item active">
                        <a className="nav-link" ><i class="fa fa-home"></i> Home</a>
                     </li>
                     <li className="nav-item">
                        <a className="nav-link" ><i class="fa fa-edit"></i> My Questions</a>
                     </li>
                     <li className="nav-item">
                        <a className="nav-link" ><i class="fa fa-edit"></i> My answers</a>
                     </li>
                     <li className="nav-item">
                        <a className="nav-link"><i class="fa fa-bell"></i> Notifications</a>
                     </li>
                  </ul>
                  <form className="form-inline my-2 my-lg-0 col-md-5" action="" method="get">
                     <input name="q" class="myform-control mr-sm-2" type="text" placeholder="Search Quora"/>
      
                  </form>
                  <ul className="navbar-nav ml-auto">
                     <li>
                        <a  id="add-question" class="btn mybtn btn-success">Add Question</a>
                     </li>
                    
                  </ul>
               </div>
            </div>
        
        );
    }
}

export default NavBar;