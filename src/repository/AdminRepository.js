import Repository from "./Repository";

const resource = "/admin";

export default {
    getMap() {
        return Repository.get(`${resource}/map`)
    }
}