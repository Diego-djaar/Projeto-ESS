export default function Button(props: {func: ()=>void, text: string, style: object, id: string}) {
    return (
        <button type="button" onClick={props.func} style={props.style} id={props.id}>
            {props.text}
        </button>
    )
}