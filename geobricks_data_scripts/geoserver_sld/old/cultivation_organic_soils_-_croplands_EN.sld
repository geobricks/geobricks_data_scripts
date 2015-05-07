<?xml version="1.0" encoding="UTF-8"?>
<sld:StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:sld="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" version="1.0.0">
    <sld:UserLayer>
        <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
        </sld:LayerFeatureConstraints>
        <sld:UserStyle>
            <sld:Name>20120812</sld:Name>
            <sld:Title/>
                <FeatureTypeStyle>
                   <Rule>
                     <RasterSymbolizer>
                       <ColorMap type="intervals">                  
                         <ColorMapEntry color="#006000" quantity="0.23689989" opacity="0.0000001" label="Ha (Hectars)" />
                         <ColorMapEntry color="#006000" quantity="10" label="0.2 - 10" />
                         <ColorMapEntry color="#7AAA00" quantity="25" label="10 - 25"/>
                         <ColorMapEntry color="#FFFF00" quantity="40" label="25 - 40"/>
                         <ColorMapEntry color="#FF9900" quantity="60" label="40 - 60"/>
                         <ColorMapEntry color="#FF2100" quantity="90" label="60 - 90"/>
                       </ColorMap>
                     </RasterSymbolizer>
                   </Rule>
               </FeatureTypeStyle>
        </sld:UserStyle>
    </sld:UserLayer>
</sld:StyledLayerDescriptor>

