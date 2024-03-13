const pages = ["signup", "login", "main"];
export function refresh_window_assign(func: () => void){
    refresh_window.push(func)
}
const refresh_window: (() => void)[] = [];
export let page_atual = window.localStorage.getItem("page_atual");
if (page_atual === null) {
    page_atual = "signup";
    window.localStorage.setItem("page_atual", page_atual);
}

export function set_page(page: string) {
    if (!pages.includes(page)) {
        console.error("página inexistente")
    }
    page_atual = page;
    window.localStorage.setItem("page_atual", page_atual);
    refresh_window.forEach(func => {
        func();
    }); 
}