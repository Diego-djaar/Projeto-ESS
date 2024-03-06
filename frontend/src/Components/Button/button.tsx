export default function Button(props: {func: ()=>void, text: string, style: object}) {
    return (
        <button type="button" onClick={props.func} style={props.style}>
            {props.text}
        </button>
    )
}