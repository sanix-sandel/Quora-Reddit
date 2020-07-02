import React, {Component} from 'react';


class SiderBarR extends Component{
    render(){
        return(
        <div class="col-lg-3">
            <div class=" q-wid">
               <div class="ui-block">
                  <h6 class="my-4">Improve Your Feed</h6>
                  
                  <div class="nav flex-column nav-pills nav-stacked" id="v-pills-tab"  aria-orientation="vertical">
                    <p class="nav-link"  data-toggle="pill"   >  Upvote 5 more good answers</p>
                    
                  </div>
                </div>
            </div>
        </div>
        );
        
    }
}

export default SiderBarR;