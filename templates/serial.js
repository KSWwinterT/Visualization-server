import React, {useState} from "react";

const Cam = () => {
    return (
        <div>
            <img
                src="http://localhost:5000/video_stream"
                alt = "Video"
            />
        </div>
    );
};

export default Cam;