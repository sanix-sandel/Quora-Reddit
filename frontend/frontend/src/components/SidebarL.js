import React, {Component} from 'react';


class SideBarL extends Component{
    render(){
        return (
        
            <div class="col-lg-2">
                <div class=" aff-right">
                    <div class="ui-block">
                        <h6 class="my-4">Feeds</h6>
                  
                        <div class="nav flex-column nav-pills nav-stacked" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                            <a class="nav-link" data-toggle="pill" > Menu</a>
                            <a class="nav-link" data-toggle="pill" > Create a Group</a>
                            <a class="nav-link" data-toggle="pill" > My groups</a>
                            <a class="nav-link" data-toggle="pill" > Groups</a>
                            
                        </div>
                    </div>
                </div>
            </div>
           
        );
    }
}

export default SideBarL;