import React, {Component} from 'react';

const Body=(props)=>{
        return (
       
            
            <div class="ui-block">
                <article class="hentry post">
                    <div class="m-link">
                        <a href="#"  target="_blank">
        <a href="{{ q.get_absolute_url }}"><h4 id="#title">{props.quest.title}</h4></a>
                        </a>
                    </div>
                    <div class="post__author author vcard inline-items">
                        <img />
                        <div class="author-date">
                            <a class="h6 post__author-name fn" href="#">submitted_by.username</a>
                            <div class="post__date">
                                <time class="published" datetime="2004-07-24T18:18">
                                    Asked 2h ago
                                </time>
                            </div>
                        </div>
                        <div class="more">
                            <a href="#">
                            <i class="fa fa-ellipsis-v"></i>
                            </a>
                        </div>
                    </div>
                    <p>
                        body
                    </p>
                    <div class="post-additional-info inline-items">
                        <p>
                            <a href="{{q.get_absolute_url}}" class="btn btn-sm btn-light"><span class="fa fa-pencil"></span> Answer</a>
                            <a href="#" class="btn btn-sm btn-light"><i class="fa fa-retweet"></i> Retweeter</a>
                        </p>
                        <p class="social-icons">
                            <a href="#" class="btn btn-sm btn-light"><i class="fa fa-facebook"></i></a>
                            <a href="#" class="btn btn-sm btn-light"> <i class="fa fa-twitter"></i></a>
                            <a href="#" class="btn btn-sm btn-light"> <i class="fa fa-share"></i></a>
                        </p>
                    </div>
                </article>
            </div>

        
            
        )
    
}

export default Body;