import AdminRepository from "./AdminRepository";

const repositorys = {
    admin: AdminRepository
}

export const RepositoryFactory = {
    get: name => repositorys[name]
}