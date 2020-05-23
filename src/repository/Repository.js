import axios from "axios";

const baseDomain = "http://localhost"
const baseURL = `${baseDomain}:8081`

export default axios.create({
    baseURL,
    auth: {
        username: 'admin',
        password: '123'
      }
      
    
})