This function sets a particular group to a color (see list of colors with get_colors).


## Reference


### Arguments

| Arguments | Type | Explanation |
| --- | --- | --- |
| group | `string`  | Name of the predefined led's group. |
| color | `string`  | Name of the predefined led's color. |



### Return
`None`

### Exceptions

* `RayaLedsWrongGroup` 
* `RayaLedsWrongColor`

See the [complete LEDs exceptions](/v2/docs/leds-exceptions){target="_blank"}.

## Usage example

Sets the 'head' group of leds to the color 'red' (see hex values in [get_colors()](/v2/docs/leds-get-colors).
Code:
``` python
self.leds.set_color(group = 'head', color = 'red')
```
